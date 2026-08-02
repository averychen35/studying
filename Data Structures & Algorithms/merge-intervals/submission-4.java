class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<int[]> output = new ArrayList<>(); // write down this syntax
        output.add(intervals[0]);
        for (int[] interval: intervals) {
            int min = interval[0];
            int max = interval[1];
            int lastEnd = output.get(output.size()-1)[1]; // grabs previous end
            if (min <= lastEnd) {
                output.get(output.size()-1)[1] = Math.max(max, lastEnd);
            }
            else {
                output.add(new int[]{min, max}); // write down this syntax
            }
        }
        return output.toArray(new int[output.size()][]); //what is this syntax
    }  
    }
