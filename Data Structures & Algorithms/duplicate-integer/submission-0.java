class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i : nums){
            if (map.containsKey(i)){
                return true;
            } 

            map.put(i, 1);
        }

        return false;
    }
}
