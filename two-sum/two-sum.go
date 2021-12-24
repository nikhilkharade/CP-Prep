import "fmt"

func twoSum(nums []int, target int) []int {
    var seen_variables  = map[int] int {
        
    }
    for i:=0;i<len(nums);i++  {
        difference := target - nums[i]
        value, ok := seen_variables[difference]
        if ok  {
            fmt.Println("value: ", value , "seem" , seen_variables , "Difference", difference)
            solution := [] int {seen_variables[difference],i};
            fmt.Println(solution)
            return solution
        }
        seen_variables[nums[i]] = i 
    }
    var no_value [] int;
    return no_value
}