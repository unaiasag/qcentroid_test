from braket.aws import AwsDevice
from braket.emulation.local_emulator import LocalEmulator
from braket.circuits import Circuit, FreeParameter
import json

def run(input_data:dict, solver_params:dict, extra_arguments:dict) -> dict:

    # Define a FreeParameter to represent the angle of a gate
    alpha = FreeParameter("alpha")

    # Define a circuit with three qubits
    my_circuit = Circuit().h(0).cnot(control=0, target=1)#.rx(0, alpha)
    print(my_circuit)

    # Instantiate the device
    ankaa3 = AwsDevice("arn:aws:braket:us-west-1::device/qpu/rigetti/Ankaa-3")
    ankaa3_properties = ankaa3.properties

    # Put the Ankaa-3 properties in a file named ankaa3_device_properties.json
    with open("ankaa3_device_properties.json", "w") as f:
        json.dump(ankaa3_properties.json(), f)

    # Load the json into the ankaa3_data_json variable
    with open("ankaa3_device_properties.json", "r") as json_file:
        ankaa3_data_json = json.load(json_file)

    # Create the Ankaa-3 local emulator from the json file you created
    ankaa3_emulator = LocalEmulator.from_json(ankaa3_data_json)
    ankaa3_emulator.run(my_circuit, shots=10)

    # ankaa3.run(my_circuit, shots=10)
    output = {"message": "Hello world!"}

    return output