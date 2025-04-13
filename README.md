1. `Forge init --force`
2. Set Python virtual environment: `python3 -m venv .venv`
3. Activate the virtual environment: `source .venv/bin/activate`
4. Install dependencies
   ```sh
   pip install pip -U
   pip install slither-analyzer -U  # solc-select 1.0.4
   solc-select install 0.8.26
   solc-select use 0.8.26
   solc --version
   ```
5. Write Contract code: [src/Bug.sol](./src/Bug.sol)
6. Run Slither: `slither src/Bug.sol`

---

7. Write Contract code: [src/HelloWorld.sol](./src/HelloWorld.sol)
8. Write Detector in a package [\_\_detectors\_\_/HelloWorldDetector.py](./__detectors__/HelloWorldDetector.py)
