from pathlib import Path

import nbformat


ROOT = Path(__file__).parents[1]
NOTEBOOKS = sorted(ROOT.glob("*.ipynb"))


def test_notebooks_are_valid_and_contain_code():
    assert NOTEBOOKS, "At least one research notebook should be present"
    for path in NOTEBOOKS:
        notebook = nbformat.read(path, as_version=4)
        nbformat.validate(notebook)
        assert any(cell.cell_type == "code" for cell in notebook.cells), path.name


def test_research_utility_has_no_machine_specific_upload_path():
    utility = (ROOT / "recreate_sentiment_plot.py").read_text()
    assert "/home/ubuntu/upload" not in utility
    assert "argparse" in utility
