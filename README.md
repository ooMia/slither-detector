# Slither Detector Practice

## Set-up
1. `git clone https://github.com/ooMia/slither-detector.git`
2. `cd slither-detector`
3. Step 2 to 4: install Python dependencies 
4. `forge install`
5. `slither src/Bug.sol`
6. `./setup.sh`
6. `slither src/HelloWorld.sol --detect hello-world`
7. `slither src/Herbicide.sol --detect herbicide`

## Progress
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

7.  Write Contract code: [src/HelloWorld.sol](./src/HelloWorld.sol)
8.  Write Detector in a package: [\_\_detectors\_\_/hello_world.py](./__detectors__/hello_world.py)
9.  Write `setup.sh` to update configuration: [setup.sh](./setup.sh)
10. Allow execution: `chmod +x setup.sh`
11. Execute for copy: `./setup.sh`
12. Add modules in importer: [\_\_detectors\_\_/all_detectors.py](./__detectors__/all_detectors.py)
13. Execute for overwrite: `./setup.sh`
14. Check the result

    ```sh
    ❯ ./setup.sh
    🔄 커스텀 detector를 Slither에 적용합니다.
    --- .venv/lib/python3.13/site-packages/slither/detectors/all_detectors.py       2025-04-14 06:18:41
    +++ __detectors__/all_detectors.py      2025-04-14 06:18:43
    @@ -107,3 +107,4 @@

    # from .statements.unused_import import UnusedImport

    +from .__detectors__.hello_world import HelloWorldDetector
    ⚠️ 변경사항이 적용됩니다.
    ✅ 설정이 완료되었습니다.
    ```

15. Run Slither: `slither src/HelloWorld.sol --detect hello-world`
16. Check the result

    ```sh
    ❯ slither src/HelloWorld.sol --detect hello-world
    ...

    INFO:Detectors:
    returns 'Hello, World!' HelloWorld.hello() (src/HelloWorld.sol#5-7)
    Reference: none
    INFO:Slither:src/HelloWorld.sol analyzed (1 contracts with 1 detectors), 1 result(s) found
    ```

---

17. Install Dependency: `forge install https://github.com/Uniswap/v4-periphery`
18. Write Contract code: [src/Herbicide.sol](./src/Herbicide.sol)
19. Write Detector in a package: [\_\_detectors\_\_/herbicide.py](./__detectors__/herbicide.py)
20. Add modules in importer: [\_\_detectors\_\_/all_detectors.py](./__detectors__/all_detectors.py)
21. Run Slither: `slither src/Herbicide.sol --detect herbicide`
22. Check the result

    ```sh
    ❯ slither src/Herbicide.sol --detect herbicide
    ...
    
    INFO:Detectors:
    Permission not implemented: _beforeSwap in contract HerbicideDetector (src/Herbicide.sol#6-31)
    Reference: none
    INFO:Slither:src/Herbicide.sol analyzed (20 contracts with 1 detectors), 1 result(s) found
    ```
