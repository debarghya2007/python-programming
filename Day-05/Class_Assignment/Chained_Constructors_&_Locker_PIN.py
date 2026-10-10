class PatientProfile:
    def __init__(self, *args):
        # Chained constructor routing (simulating Java's this(...))
        if len(args) == 0:
            # 1. No-arg constructor: PatientProfile() -> calls this(None, None)
            self._this(None, None)
        elif len(args) == 1:
            # 2. Name-only constructor: PatientProfile(name) -> calls this(None, name)
            self._this(None, args[0])
        elif len(args) == 2:
            # 3. ID + Name constructor: PatientProfile(patient_id, name)
            self._this(args[0], args[1])
        else:
            raise TypeError("Invalid number of constructor arguments")

    def _this(self, patient_id: str | None, name: str | None) -> None:
        """Central initialization logic linked via constructor chaining."""
        self._patient_id = None
        if patient_id is not None:
            self.set_patient_id(patient_id)
            
        self._name = name
        self._discharged = False
        self._locker_pin = None  # Write-only field

    # --- JavaBean-compliant Getters & Setters ---

    def get_patient_id(self) -> str | None:
        return self._patient_id

    def set_patient_id(self, patient_id: str) -> None:
        """Write-once property: takes effect only once, ever."""
        if self._patient_id is None and patient_id is not None:
            self._patient_id = patient_id

    def get_name(self) -> str | None:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    def is_discharged(self) -> bool:
        return self._discharged

    def set_discharged(self, discharged: bool) -> None:
        self._discharged = discharged

    def set_locker_pin(self, pin: str) -> None:
        """Write-only property: sets the locker PIN without any getter method."""
        # Optional deterministic hash/storage for write-only PIN
        self._locker_pin = hash(pin)

    # Java-style camelCase alias methods for seamless test compatibility
    getPatientId = get_patient_id
    setPatientId = set_patient_id
    getName = get_name
    setName = set_name
    isDischarged = is_discharged
    setDischarged = set_discharged
    setLockerPin = set_locker_pin


if __name__ == "__main__":
    # --- Example 1: Name-only constructor (ID remains None) ---
    p1 = PatientProfile("Arjun Iyer")
    print(f'Patient ID: {p1.getPatientId()}')
    # Output: None (null)

    # --- Example 2: ID + Name constructor ---
    p2 = PatientProfile("MT2026-0142", "Arjun Iyer")
    print(f'Patient ID: {p2.getPatientId()}')
    # Output: "MT2026-0142"

    # --- Example 3: Write-once patientId test ---
    p3 = PatientProfile()
    p3.setPatientId("MT2026-0142")
    p3.setPatientId("HACKED-0000")  # Silently ignored!
    print(f'Patient ID after hack attempt: {p3.getPatientId()}')
    # Output: "MT2026-0142"

    # --- Example 4: Write-only Locker PIN ---
    p3.setLockerPin("1234")
    # No getLockerPin method exists to retrieve the PIN, keeping it strictly write-only
