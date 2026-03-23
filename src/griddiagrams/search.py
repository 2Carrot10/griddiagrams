import pandas as pd
import ast
from pathlib import Path
from typing import List
from .core import *
from pathlib import Path
from .plotting import plot_grid_diagram
from .data import get_all_knot_names, get_vlist_by_name, load_knot_data
import json
from sys import argv

unsolved_knot_names = ["12n_79", "12_168", "13n_282" , "13n_917" , "13n_1279" , "13n_1281" , "13n_1413", "13n_1826" , "13n_2915" , "13n_3089" , "13n_3904" , "13n_3932"]


def find_nice_for_all_knots(search_function, path_name, depth = 50, print_function=print_clean):
    """
    Options for search_function are gridstate_finder_commute, gridstate_finder_stab
    Options for print_function are print_clean, print_vertlist
    """
    find_nice_for_knots(get_all_knot_names(), search_function, path_name, depth, print_function)

def find_nice_for_knots(knots, search_function, path_name, depth = 50, print_function=print_clean):
    try:
        path_name = Path(path_name)
        for knot in knots:
            knot_vlist = get_vlist_by_name(knot)
            result = search_function(get_vlist_by_name(knot), depth)
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

def find_nice_for_unsolved(search_function, path_name, depth = 50, print_function=print_clean):
    find_nice_for_knots(unsolved_knot_names, search_function, path_name, depth, print_function)

if __name__ == "__main__":
    load_knot_data()

    if argv[-1] == "unsolved":
        find_nice_for_unsolved(gridstate_finder_commute, '../output/')
    else:
        find_nice_for_all_knots(gridstate_finder_commute, '../output-unsolved/')
