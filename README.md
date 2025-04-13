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
8. Write Detector in a package: [\_\_detectors\_\_/HelloWorldDetector.py](./__detectors__/HelloWorldDetector.py)
9. Write `setup.sh` to update configuration: [setup.sh](./setup.sh)
10. Allow execution: `chmod +x setup.sh`
11. Execute for copy: `./setup.sh`
12. Add modules in importer: [\_\_detectors\_\_/all_detectors.py](./__detectors__/all_detectors.py)
13. Execute for overwrite: `./setup.sh`
14. Check the result

    ```sh
    ❯ ./setup.sh
    🔄 커스텀 detector를 Slither에 적용합니다.
    --- .venv/lib/python3.13/site-packages/slither/detectors/all_detectors.py       2025-04-14 06:05:41
    +++ __detectors__/all_detectors.py      2025-04-14 06:05:43
    @@ -107,3 +107,4 @@

    # from .statements.unused_import import UnusedImport

    +from .__detectors__.HelloWorld import HelloWorldDetector
    ⚠️ 변경사항이 적용됩니다.
    ✅ 설정이 완료되었습니다.
    ```
