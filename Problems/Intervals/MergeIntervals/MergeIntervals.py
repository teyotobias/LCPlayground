# As an observation, it seems that my solutions tend to be much more time-efficient than space-efficient. Learn about the causes and effects of the trade offs. Applications useful?

def mergeIntervals(intervals):
    #Flow: 
            #need a list to store return intervals
            #sort intervals by start time
            #go through list -> if no intervals in list yet 
                                #OR if new interval start time DOES NOT overlap with most recent interval end time, append it.
            #ELSE: check if new end time > previous end time, max function, make end time latest possible
            ret = []
            intervals = sorted(intervals, key=lambda x: x[0])
            for interval in intervals:
                              #new start time > previous end time? Easy append
                if not ret or interval[0] > ret[-1][1]:
                    ret.append(interval)
                    #if not, then clearly there is an overlap
                    #don't need to worry about start times, this is what the sort was for
                else:
                    #need to find appropriate end time for no overlap
                    ret[-1][1] = max(interval[1], ret[-1][1])
            return ret
