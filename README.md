# Visualization

This repository uses Jupyter Notebook for data visualization from results generated by the post processor.  The post processor can be found [here](https://github.com/UTMediaCAT/Post-processor).

# Prerequisites

You will need:
- Python3
	- jupyter
	- pandas
	- matplotlib
	- d3graph
 	- plotly
- *.csv* file from post processor

As long as you have the **pip** command line tool, the modules should be automatically installed when you run the main script.  If there is an error installing the modules, whether it be due to user permissions or other reasons, run `pip install -r requirements.txt`

# Instructions

1. Place the *.csv* file generated from the post processor inside the Jupyter Notebook by following [these instructions](https://github.com/UTMediaCAT/Visualization/tree/main/notebooks)
2. Call `python3 main.py`

The Jupyter Notebook should open in a web browser and be ready to visualize the data provided by the given *.csv* file.

# Exporting Notebooks

If you would like to export Jupyter Notebooks into a different format like *pdf*, *LaTeX*, or *Markdown*, you can use [nbconvert](https://nbconvert.readthedocs.io/en/latest/).  Note that you may need to install pandoc in order to export to a different output format.  To install pandoc, run `pip install pandoc` or download from [here](https://pandoc.org/installing.html).

To export, follow these instructions:
1. Change into the directory with the Jupyter Notebook in the *notebooks* directory
2. Call `jupyter nbconvert <notebook> --to <format>` where *notebook* is an existing Jupyter Notebook and *format* is the format type you want to export to.  For example, `jupyter nbconvert stack_are_chart.ipynb --to pdf` will convert the stack area chart notebook to a PDF document.

