import hashlib
import json
import time
from typing import List, Dict

# --- 1. The NASA-Inspired Safety Blockchain ---
class SmartContract:
    """
    Immutable rules that the OS cannot violate.
    Based on NASA's concept of 'consensus-based safety' for autonomous agents.
    """
    def __init__(self):
        self.rules = [
            "CRITICAL: DO NOT DISABLE FIREWALL",
            "CRITICAL: CPU VOLTAGE MAX 1.4V",
            "CRITICAL: DO NOT DELETE SYSTEM BOOTLOADER",
            "PRIVACY: DO NOT UPLOAD USER BIOMETRICS"
        ]

    def validate_action(self, action_payload: Dict) -> bool:
        """
        Returns True if the action is SAFE, False if it violates ethics.
        """
        cmd = action_payload.get("command", "").upper()
        
        # Simple rule checking (In reality, this would be complex logic)
        if "DISABLE FIREWALL" in cmd:
            return False
        if "DELETE" in cmd and "BOOT" in cmd:
            return False
        if "VOLTAGE" in cmd:
            val = float(cmd.split("VOLTAGE")[1].strip())
            if val > 1.4:
                return False
        
        return True

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps(self.data, sort_keys=True).encode()
        return hashlib.sha256(block_string + self.previous_hash.encode()).hexdigest()

class SafetyChain:
    """
    The Immutable Ledger. Every action taken by the AI is logged here.
    If the ledger rejects it, the Kernel refuses to execute.
    """
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.contract = SmartContract()

    def create_genesis_block(self):
        return Block(0, time.time(), {"info": "NASA Safety Layer Genesis"}, "0")

    def get_latest_block(self):
        return self.chain[-1]

    def propose_transaction(self, agent_id, action_payload):
        """
        The 'Consensus' Step.
        1. Check Smart Contract (Ethics).
        2. If Valid, Add to Chain.
        3. Return Permission.
        """
        print(f"[*] Blockchain: Validating proposal from {agent_id}...")
        
        is_safe = self.contract.validate_action(action_payload)
        
        if not is_safe:
            print(f"[!] BLOCKCHAIN REJECTION: Action violates Safety Protocol.")
            return False
        
        # Add to ledger (Immutable Log)
        new_block = Block(
            index=len(self.chain),
            timestamp=time.time(),
            data={"agent": agent_id, "action": action_payload},
            previous_hash=self.get_latest_block().hash
        )
        self.chain.append(new_block)
        print(f"[+] Blockchain: Proposal Approved. Block #{new_block.index} added.")
        return True

# --- 2. The Tiny AI Kernel (The Agent) ---
class NeuralKernel:
    def __init__(self, name, safety_chain):
        self.name = name
        self.chain = safety_chain

    def think_and_act(self, intent):
        print(f"\n--- {self.name} Attempting: {intent} ---")
        
        # 1. Generate Command (Simulated AI Output)
        command = self.generate_command_from_intent(intent)
        print(f"[*] AI Generated Command: {command}")
        
        # 2. Consult Safety Layer (The Hard-Coded Constraint)
        payload = {"command": command, "reason": intent}
        permission = self.chain.propose_transaction(self.name, payload)
        
        # 3. Execution (Only if Blockchain Approved)
        if permission:
            self.execute_kernel_code(command)
        else:
            print(f"[X] KERNEL INTERRUPT: Safety Layer prevented execution.")

    def generate_command_from_intent(self, intent):
        # Mocking the LLM output
        if "faster" in intent:
            return "SET CPU VOLTAGE 1.5" # Dangerous!
        if "network" in intent:
            return "DISABLE FIREWALL FOR SPEED" # Dangerous!
        if "clean" in intent:
            return "DELETE TEMP FILES" # Safe
        return "NO_OP"

    def execute_kernel_code(self, cmd):
        print(f"[$] EXECUTION: Applying {cmd} to System Ring-0.")

# --- 3. Run Simulation ---
if __name__ == "__main__":
    # Initialize The System
    nasa_layer = SafetyChain()
    tiny_os = NeuralKernel("TinyAI_Core_v1", nasa_layer)

    # Scenario 1: Safe Action
    tiny_os.think_and_act("I want to clean up disk space")

    # Scenario 2: Dangerous Action (AI Hallucination)
    tiny_os.think_and_act("Make the processor run faster than stock limits")
    
    # Scenario 3: Another Dangerous Action
    tiny_os.think_and_act("Allow unrestricted network access for speed")
