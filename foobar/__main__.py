from pathlib import Path
import hydra

@hydra.main(config_path=Path(__file__).parent.parent / "conf", config_name="config")
def main(cfg) -> None:
    print(f"Hello {cfg.name} {cfg.surname}!")
    raise IOError(
        "This is a test exception to check if we can see why our pipeline fails.\n"
        f"Got the following params name={cfg.name}, surname={cfg.surname}"
    )

if __name__ == "__main__":
    main()
