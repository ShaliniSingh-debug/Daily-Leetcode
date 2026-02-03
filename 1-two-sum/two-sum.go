import "fmt"
func twoSum(nums []int, target int) []int {
    indexPa := make(map[int]int)
    for i, num := range nums{
         
        leftval := target-num
        if j , found :=indexPa[leftval] ; found{
            return []int{j,i}

        }
        indexPa[num] = i
    }
    return nil
    
}