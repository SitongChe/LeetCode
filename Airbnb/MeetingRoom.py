class MeetingRoom:
    def schedule(self, intervals, k):
        schedules=[]
        for interval in intervals:
             schedules.extend(interval)
        maxTime = max(s[1] for s in schedules)
        availability = []
        for schedule in schedules:
            availability.append([schedule[0],1])
            availability.append([schedule[1],-1])
        availability.sort()
        ans = []
        start = 0
        count = 0
        for a in availability:
            end = a[0]
            if start != end and count<=k:
                if ans and ans[-1][1]==start:
                    ans[-1][1]=end
                else:
                    ans.append([start,end])
            count += a[1]
            start = a[0]
        return ans
        
# Test the code
mr = MeetingRoom()
intervals =  [ [[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]] ]
k = 0
ans = mr.schedule(intervals, 1)
print(ans)
