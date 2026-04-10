# 📄 Publish–Subscribe Notification Service


---

## 1. Introduction

This project implements a **Publish–Subscribe Notification Service** using **TCP sockets in Python**. The system enables communication between multiple clients where publishers send messages to specific topics, and subscribers receive messages based on their subscriptions.

The system is designed to support **concurrent clients, secure communication, and real-time event delivery**.

---

## 2. Objectives

* To design a **socket-based publish–subscribe system**
* To support **multiple clients simultaneously**
* To implement **topic-based message routing**
* To ensure **secure communication using SSL**
* To evaluate **performance, scalability, and system robustness**

---

## 3. System Design

### 3.1 Architecture

The system follows a **broker-based architecture**:

Publisher → Server (Broker) → Subscribers

* The **server** acts as a central broker
* **Publishers** send messages to topics
* **Subscribers** receive messages based on subscribed topics

---

### 3.2 Components

#### a) Server

* Handles client connections
* Maintains topic–subscriber mapping
* Routes messages efficiently

#### b) Publisher

* Sends messages to specific topics

#### c) Subscriber

* Subscribes to topics
* Receives real-time notifications

---

### 3.3 Data Structure

A dictionary is used for subscription management:

```
Topic → Set of subscriber sockets
```

This ensures efficient lookup and avoids duplicate entries.

---

## 4. Implementation Details

* Programming Language: Python
* Communication Protocol: TCP
* Concurrency: Threading
* Security: SSL/TLS

The server uses **multi-threading** to handle multiple clients concurrently.

---

## 5. Performance Evaluation

### 5.1 Latency

Latency is defined as the time taken for a message to travel from the publisher to the subscriber.

```
Latency = Receive Time – Send Time
```

Observed latency was low, indicating efficient real-time communication.

---

### 5.2 Throughput

Throughput is defined as the number of messages processed per second.

```
Throughput = Number of Messages / Time
```

Throughput increases with higher message rates, demonstrating system efficiency under load.

---

### 5.3 Scalability Testing

A load testing script (`load_test.py`) was used to simulate multiple clients.

* Tested with up to **30–50 concurrent subscribers**
* System successfully handled increased load
* Slight increase in latency observed under heavy load

---

## 6. Failure Handling

The system was tested under various failure scenarios:

### a) Client Disconnection

* Handled using exception handling
* Disconnected clients are removed automatically

### b) Connection Errors

* Errors such as **Broken Pipe** and **Connection Reset** are handled without crashing

### c) Invalid Commands

* Server validates input and responds appropriately

The system remains stable under failure conditions.

---

## 7. Optimization Techniques

* Used **set data structure** for faster subscription management
* Implemented **safe iteration** to avoid runtime errors
* Enabled **socket reuse** to prevent port conflicts
* Efficient message routing mechanism

These optimizations improved performance and system stability.

---

## 8. Security Implementation

Secure communication is implemented using **SSL/TLS**.

* `cert.pem` → Public certificate
* `key.pem` → Private key

This ensures encrypted communication between clients and server.

---

## 9. Results

* Successfully implemented a **publish–subscribe system**
* Achieved **real-time message delivery**
* Supported **multiple concurrent clients**
* Demonstrated **secure communication**
* Evaluated **performance and scalability**
* Handled failures effectively

---

## 10. Applications

* Notification systems
* Messaging systems
* Event-driven architectures
* IoT communication

---

## 11. Conclusion

The project successfully demonstrates a **scalable, secure, and efficient publish–subscribe architecture** using TCP sockets. The system performs well under load, handles failures gracefully, and provides real-time communication.

---



