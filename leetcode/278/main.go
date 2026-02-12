//go:build ignore

package main

/**
 * Forward declaration of isBadVersion API.
 * @param   version   your guess about first bad version
 * @return 	 	      true if current version is bad
 *			          false if current version is good
 * func isBadVersion(version int) bool;
 */

func isBadVersion(version int) bool {
    return false // stub
}

func firstBadVersion(n int) int {
    minVal := 1
    maxVal := n
    for minVal <= maxVal{
        mid := minVal + (maxVal-minVal)/2
        if isBadVersion(mid) {
            maxVal = mid - 1
        }else{
            minVal = mid + 1
        }
    }
    return minVal
}