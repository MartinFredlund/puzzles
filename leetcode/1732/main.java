class Solution {
    public int largestAltitude(int[] gain) {
        int altitude = 0;
        int maxAltitude = 0;
        for (int change: gain){
            altitude += change;
            maxAltitude = Math.max(altitude, maxAltitude);
        }
        return maxAltitude;
    }
}