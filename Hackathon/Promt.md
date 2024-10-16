# Qiskit Fall Festival 2024 at IIT Jodhpur 

# Hackathon Prompt: Quantum Random Number Generator

## Background and Motivation
Did you know that random number generators are a valuable tool for computing? Real random number generation is incredibly important for things like security and cryptography. However, all "random number generators" from classical computers aren’t really... random.

Your prompt is to create a truly random number generator using a quantum processor.

## Getting Started
Your task is to create a random number generating circuit. You can decide on the number of qubits and possible outcomes, we’ll call this number `n`. Keep in mind that creating a superposition chain of more than 10 qubits can be quite tricky.

### Steps:
- Utilizing **H-gates**, generate a quantum state with `n` number of equally possible outcomes.
- Think about how many qubits are needed for this task and how the quantum computational space scales with each additional qubit.
- Assign numeric values to the possible states, so that the measured state of the qubits results in your program printing the associated value.

### Tips:
- Define how many times your quantum circuit is run by setting the number of **“shots”**.
  - Running your circuit once creates the quantum state with `n` equally possible outcomes.
  - Running it multiple times will give you a better demonstration of the quantum state’s superposition.
  - Each run will show how the possible outcomes behave across multiple measurements.

- **Example:**
  - After running multiple shots, you should observe the results filling `n` equal buckets, showing that each quantum state was equally likely to be measured.
  - However, running it once will give you just one result, which serves as the random number output.

### Deeper Questions:
As you run more and more "shots", you might find that some numbers are returned more often than others. This is due to **intrinsic noise** in the quantum system. 

Your next challenge is to **mitigate noise**. You may explore:
- Why are some values more likely to be returned than others?
- What error mitigation techniques can you implement to make the random number generator as "fair" as possible?

There are several error mitigation techniques that can be explored, such as:
- **Readout error correction**
- **Zero-noise extrapolation**
- **Pauli twirling**

---

### Resources:
- **Basics of Quantum Information**
- **Quantum Magic Eight Ball**
- **Qiskit Fall Fest 2024 Notebook 1**
- **Error Mitigation and Suppression Techniques Documentation**


Good luck!


# Points Distribution

## 1. Technical Aspects (30 total points)
- **Complexity of Algorithm**
- **Well-optimized code**
- **Scalability**
- **Ease of use and intuitive for end users**
- **Using significant parts of the Qiskit SDK, Qiskit Runtime, or other parts of the Qiskit ecosystem**

## 2. Originality and Uniqueness (25 total points)
- **Uniqueness compared to others**
- **Novelty**
- **Interesting aspects**

## 3. Usefulness and Complexity (25 total points)
- **Well-designed and most useful**
- **Functionality while testing**
- **Real-world business applications or valuable tool for individuals**
- **Potential for further building out and refinement**

## 4. Presentation (20 total points)
- **Team Presentation**
- **Technical explanation**
- **Team involvement**
- **Cohesive storytelling**
