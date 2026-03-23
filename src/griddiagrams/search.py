import pandas as pd
import ast
from pathlib import Path
from typing import List
from .core import *
from pathlib import Path
from .plotting import plot_grid_diagram
from .data import get_all_knot_names, get_vlist_by_name, load_knot_data
import json

# Options for search_function are gridstate_finder_commute, gridstate_finder_stab
# Options for print_function are print_clean, print_vertlist
def find_nice_for_all_knots(search_function, path_name, depth = 50, print_function=print_clean):
    try:
        path_name = Path(path_name)
        for knot in get_all_knot_names():
            knot_vlist = get_vlist_by_name(knot)
            result = gridstate_finder_commute(get_vlist_by_name(knot), depth)
            if result:
                nice_grid = result["vlist"]
                winding_matrix = result["matrix"]
                perfect_state = result["gridstate"]
                alex = result["alexander-grading"]

                print("----")
                print("***", knot)
                print_function(knot_vlist)
                print("Nice knot found")
                print_function(nice_grid)
                print("Alex grading", alex)
                print("Winding matrix", winding_matrix)

                X2, O2 = vlist_to_XO(nice_grid)

                fig = plot_grid_diagram(
                    X=X2,
                    O=O2,
                    matrix=winding_matrix,
                    P=perfect_state,
                    knot_name=knot,
                )
                png_path = format(path_name / f"nice_diagram_{knot}.png")
                json_path = format(path_name / f"nice_diagram_{knot}.json")

                fig.savefig(png_path, dpi=300, bbox_inches="tight")

                with open(json_path, "w") as f:
                    json.dump(result, f)
            else:
                print(
                    f"No nice grid diagram found for {knot} using {search_function.__name__} at depth {depth}. "
                    "Try increasing the depth or including a more powerful search function."
                )
    except KeyboardInterrupt:
        print("ctrl+C")
        pass

if __name__ == "__main__":
    load_knot_data()
    find_nice_for_all_knots(gridstate_finder_commute, '../output/')
