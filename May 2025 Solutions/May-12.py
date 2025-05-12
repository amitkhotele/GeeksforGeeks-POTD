import heapq

class Solution:
    def mostBooked(self, n, meetings):
        meetings.sort()  # Sort by start time
        available_rooms = list(range(n))  # All room numbers available
        heapq.heapify(available_rooms)
        ongoing_meetings = []  # (end_time, room_number)
        meeting_count = [0] * n
        
        for start, end in meetings:
            # Free up rooms whose meetings have ended
            while ongoing_meetings and ongoing_meetings[0][0] <= start:
                end_time, room = heapq.heappop(ongoing_meetings)
                heapq.heappush(available_rooms, room)

            duration = end - start

            if available_rooms:
                # Assign the meeting to the smallest room
                room = heapq.heappop(available_rooms)
                heapq.heappush(ongoing_meetings, (end, room))
            else:
                # Delay the meeting
                earliest_end, room = heapq.heappop(ongoing_meetings)
                heapq.heappush(ongoing_meetings, (earliest_end + duration, room))

            meeting_count[room] += 1

        # Find the room with the most meetings
        max_meetings = max(meeting_count)
        for i in range(n):
            if meeting_count[i] == max_meetings:
                return i
