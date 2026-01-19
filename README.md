# Tiny AI + NASA Safety Chain: The Ethics Kernel

## Concept
This project demonstrates a "Safety-First" Operating System architecture where a **Tiny AI** (the Spinal Cord) is supervised by a **Blockchain Ledger** (The Conscience).

This is based on NASA's research into **Resilient Networking and Computing (RNCP)** and **Consensus-Based Safety** for autonomous agents.

## Architecture

### 1. The Proposer: NeuralKernel (Tiny AI)
*   **Role:** Analyzes system state and proposes optimizations (e.g., "Overclock CPU", "Open Port 80").
*   **Model:** A <2GB edge-optimized LLM (e.g., Llama-3-Tiny, RWKV).
*   **Privilege:** Cannot execute directly. Must submit a "Proposal Transaction".

### 2. The Validator: SafetyChain (Blockchain)
*   **Role:** A local, lightweight, permissioned blockchain.
*   **Mechanism:** Runs **Smart Contracts** containing immutable ethical/safety rules.
    *   *Rule 1:* Max Voltage < 1.4V.
    *   *Rule 2:* Firewall must remain ACTIVE.
    *   *Rule 3:* Bootloader is Read-Only.
*   **Outcome:** If the AI's proposal violates a rule, the transaction is rejected. The OS Kernel never sees the command.

## Usage
Run the simulation to see the "Hallucination Defense" in action:
`ash
python safety_simulation.py
`

## Integration Path
To build this into a real OS:
1.  **Ledger Storage:** Use the TPM (Trusted Platform Module) or a secure enclave (Intel SGX) to store the chain.
2.  **Kernel Hook:** Write a Linux Kernel Module (LKM) that intercepts all syscalls from the AI process and verifies them against the Ledger.
