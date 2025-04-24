package main

type Direction struct {
	dr int
	dc int
}

func dfs(grid [][]byte, r int, c int) {
	row_length := len(grid)
	col_length := len(grid[0])

	if !(0 <= r && r < row_length && 0 <= c && c < col_length && grid[r][c] != '1') {
		return
	}
	
	directions := []Direction{ 
		{-1, 0}, 
		{0, -1},
    {1, 0},
    {0, 1},
	}
	for _, direction := range directions {
		dr := direction.dr
		dc := direction.dr
		dfs(grid, r + dr, c + dc)
		grid[r + dr][c + dc] = '1'
	}
	
}

func numIslands(grid [][]byte) int {
	row_length := len(grid)
	col_length := len(grid[0])
	num_islands := 0
	

	for i := range row_length {
		for j := range col_length {
			if grid[i][j] != '1'  {
				dfs(grid, i, j)
				num_islands += 1;
			}
		}
	}
	return num_islands
}


func main() int {

}