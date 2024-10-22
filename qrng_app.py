#use path streamlit run qrng_app.py on terminal to run this program
import streamlit as st
from qiskit import *
from qiskit_aer import Aer
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import *
from qiskit_aer import QasmSimulator

st.title("Quantum Random Number Generator")

# Input field for number of qubits (bitstring length)
n = st.number_input("Enter the length of bitstring (number of qubits):", min_value=1, value=1)

# Create a Quantum Circuit
qc = QuantumCircuit(n, n)

# Apply Hadamard gate to all qubits to create superposition
for i in range(n):
    qc.h(i)
    qc.measure(i, i)

# Display the quantum circuit diagram
#st.write("### Quantum Circuit:")
#st.pyplot(qc.draw('mpl'))

# Run the circuit on a simulator when button is clicked
if st.button("Generate Random Number"):
    simulator = Aer.get_backend('qasm_simulator')
    job = simulator.run(qc, shots=1)
    result = job.result().get_counts()
    
    # Extract the random bitstring and convert to decimal
    random_bitstring = list(result.keys())[0]
    random_number = int(random_bitstring, 2)
    
    # Display the random number
    st.write(f"### The generated random number is: {random_number}")
    
    # Display the measurement outcome (bitstring)
    st.write(f"### The generated random bitstring is: {random_bitstring}")
