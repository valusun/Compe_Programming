from pathlib import Path, PurePosixPath


def setting_rust_analyzer(cargo_file_paths: list[Path]) -> None:
    """`.vscode/settings.json`を作成し、rust-analyzerが動くように設定する"""

    settings_file = Path("./.vscode/settings.json").resolve()
    settings_file.unlink(missing_ok=True)
    settings_file.touch()
    # HACK: jsonで機能するファイルパスにあわせるため`PurePosixPath`に変換を噛ませているが綺麗じゃない
    formatted_path = ",\n".join([f'"{PurePosixPath(p)}"' for p in cargo_file_paths])
    writing_data = f'{{"rust-analyzer.linkedProjects":[{formatted_path}]}}'
    with open(settings_file, "w") as sf:
        sf.write(writing_data)


# 単体でも使えるように
if __name__ == "__main__":
    cargo_file_paths: list[Path] = []
    while len(s := input()):
        cargo_file_paths.append(Path(s).resolve())
    setting_rust_analyzer(cargo_file_paths)
