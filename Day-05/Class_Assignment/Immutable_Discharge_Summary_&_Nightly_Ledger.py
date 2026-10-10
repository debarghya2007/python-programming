import re


class DischargeSummary:
    # Class-level static pattern compilation
    MED_CODE_PATTERN = re.compile(r"^MED-[A-Z]$")

    def __init__(self, patient_id: str, medication_codes: list[str]):
        # Validate all medication codes before assigning
        for code in medication_codes:
            if not self.MED_CODE_PATTERN.match(code):
                raise ValueError("construction rejected")

        # Defensive copy on input to preserve immutability
        self._patient_id = patient_id
        self._medication_codes = list(medication_codes)

    @property
    def patient_id(self) -> str:
        return self._patient_id

    def get_patient_id(self) -> str:
        return self._patient_id

    def get_medication_codes(self) -> list[str]:
        """Returns a defensive copy of medication codes to prevent external tampering."""
        return list(self._medication_codes)

    def with_corrected_medication(self, index: int, new_code: str) -> 'DischargeSummary':
        """
        Wither pattern: Returns a brand-new DischargeSummary instance with 
        the updated medication code, preserving immutability of original.
        """
        if not self.MED_CODE_PATTERN.match(new_code):
            raise ValueError("construction rejected")

        updated_codes = self.get_medication_codes()
        updated_codes[index] = new_code

        # Return a new instance depending on the actual class type
        return type(self)(self._patient_id, updated_codes)

    # Java-style camelCase alias methods
    getPatientId = get_patient_id
    getMedicationCodes = get_medication_codes
    withCorrectedMedication = with_corrected_medication


class CriticalCareDischargeSummary(DischargeSummary):
    def __init__(self, patient_id: str, medication_codes: list[str], icu_days: int):
        super().__init__(patient_id, medication_codes)
        self._icu_days = icu_days

    @property
    def icu_days(self) -> int:
        return self._icu_days

    def get_icu_days(self) -> int:
        return self._icu_days

    getIcuDays = get_icu_days


def process_nightly_batch(summaries: list[DischargeSummary | None]) -> str:
    """
    Reconciles a night's worth of discharges without crashing on None/null entries.
    Uses isinstance to categorize CriticalCare vs Routine summaries.
    """
    processed = 0
    null_skipped = 0
    critical_care = 0
    routine = 0

    if summaries is None:
        return "0 processed | 0 null skipped | 0 critical-care | 0 routine"

    for summary in summaries:
        if summary is None:
            null_skipped += 1
        elif isinstance(summary, CriticalCareDischargeSummary):
            processed += 1
            critical_care += 1
        elif isinstance(summary, DischargeSummary):
            processed += 1
            routine += 1

    return f"{processed} processed | {null_skipped} null skipped | {critical_care} critical-care | {routine} routine"


# Java-style static alias function
processNightlyBatch = process_nightly_batch


if __name__ == "__main__":
    # --- Example 1: Invalid Medication Code Format Rejection ---
    try:
        invalid_summary = DischargeSummary("MT2026-0142", ["MED-A", "bad"])
    except ValueError as e:
        print(f"new DischargeSummary(\"MT2026-0142\", [\"MED-A\", \"bad\"]): {e}")
    # Output: construction rejected[cite: 17]

    # --- Example 2: Immutability & Defensive Copy Verification ---
    d = DischargeSummary("MT2026-0142", ["MED-A", "MED-B"])
    codes = d.getMedicationCodes()
    codes[0] = "TAMPERED"  # Attempt to mutate returned array
    print(f"Code after external mutation attempt: {d.getMedicationCodes()[0]}")
    # Output: "MED-A"[cite: 17]

    # --- Example 3: Nightly Ledger Batch Processing with Null Safety ---
    batch = [
        CriticalCareDischargeSummary("MT001", ["MED-X"], 4),
        None,
        DischargeSummary("MT002", ["MED-Y"])
    ]
    summary_report = process_nightly_batch(batch)
    print(summary_report)
    # Output: "2 processed | 1 null skipped | 1 critical-care | 1 routine"[cite: 18]

    # --- Example 4: Wither Method (Immutable Modification) ---
    updated_d = d.with_corrected_medication(0, "MED-Z")
    print(f"Original summary code[0]: {d.getMedicationCodes()[0]}")
    print(f"New summary code[0]: {updated_d.getMedicationCodes()[0]}")
    # Output: MED-A and MED-Z (original unchanged)
