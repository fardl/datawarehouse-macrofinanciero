import sys
import subprocess

steps =   [
        "etl/load_staging.py",
        "etl/load_dimensions.py",
        "etl/load_facts.py"
    ]

for step in steps:
    print(
        f"Ejecutando {step}..."
    )


    subprocess.run(
        [
            sys.executable,
            step
        ],
        check=True
    )

print(
    "Pipeline ejecutado correctamente"
)