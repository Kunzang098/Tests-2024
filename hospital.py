from queue import Queue

def main():
    patient_queue = Queue()

    while True:
        print("\n=== Patient Registration and Appointment Scheduling ===")
        print("1. Register Patient")
        print("2. Remove Patient after Meeting Doctor")
        print("3. Display Patient Queue")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            register_patient(patient_queue)
        elif choice == "2":
            remove_patient(patient_queue)
        elif choice == "3":
            display_queue(patient_queue)
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def register_patient(queue):
    patient_name = input("Enter patient name: ")
    queue.put(patient_name)
    print(f"Patient '{patient_name}' registered.")

def remove_patient(queue):
    if queue.empty():
        print("No patients in the queue.")
    else:
        removed_patient = queue.get()
        print(f"Patient '{removed_patient}' removed after meeting the doctor.")

def display_queue(queue):
    if queue.empty():
        print("No patients in the queue.")
    else:
        print("Current Patient Queue:")
        for index, patient in enumerate(list(queue.queue), start=1):
            print(f"{index}. {patient}")

if __name__ == "__main__":
    main()