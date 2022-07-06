from pathlib import Path
import hydra

@hydra.main(config_path=Path(__file__).parent.parent / "conf", config_name="config")
def main(cfg) -> None:
    print(f"Hello {cfg.name} {cfg.surname}!")
if __name__ == "__main__":
    main()
