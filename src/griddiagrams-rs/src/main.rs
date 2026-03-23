use std::sync::Arc;

fn main() {
    println!("Hello, world!");
}

type GridList = Vec<i32>;
type GridNotation = Vec<Vec<i32>>;
type VertList = Vec<Vec<(i32, i32)>>;
type HorzList = Vec<Vec<(i32, i32)>>;
type Permutation = Vec<i32>;
type WindingMatrix = Vec<i32>; 

/// Convert gridnotation to grid list representation.
/// 
/// Parameters
/// ----------
/// gridnotation : List[List[int]]
///     Grid notation specifying a grid diagram
///     (Grid notation is the representation of grid diagrams used in the source database from knotinfo)
///
/// Returns
/// -------
/// List[int]
///     Grid list representation, an intermediate format
fn gridnotation_to_gridlist(gridnotation: GridNotation) -> Result<GridList, String> {
    // Ensure size is a square
    if gridnotation.len() == 0 {
        return Result::Err("Grid notation cannot be empty".into());
    }

    let mut temp = [gridnotation[0][1]];
    let grid_len = gridnotation.len();
    let current_tuple = &gridnotation[0];

    while temp.len() < grid_len {
        if temp.len() % 2 == 1 {
            // Look for matching first coordinate
            for segment in &gridnotation {
                if segment[1] == temp[temp.len() - 2] {
                }
            }
        }
    }

    return todo!();
}


fn generate_array<const N: usize>() -> [[u32; N]; N] {
    todo!()
}
