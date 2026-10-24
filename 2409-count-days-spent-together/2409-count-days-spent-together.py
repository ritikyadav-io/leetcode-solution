class Solution:

    def countDaysTogether(
        self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str
    ) -> int:
        # Har mahine ke din (Non-leap year)
        days_in_months =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 

        # 1. Helper function: "MM-DD" ko 1-365 day number mein badalne ke liye
        def date_to_day(date_str: str) -> int:
            month = int(date_str[:2])  # Shuru ke 2 chars yaani Month
            day = int(date_str[3:])  # Baad ke 2 chars yaani Day
            # Pichle saare mahino ke din + current mahine ke din
            return sum(days_in_months[: month - 1]) + day

        # 2. Dono ke aane aur jaane ke din calculate karo
        alice_start = date_to_day(arriveAlice)
        alice_end = date_to_day(leaveAlice)
        bob_start = date_to_day(arriveBob)
        bob_end = date_to_day(leaveBob)

        # 3. Overlap window nikaalo
        start_together = max(alice_start, bob_start)  # Jo late aaya
        end_together = min(alice_end, bob_end)  # Jo pehle gaya

        # 4. Total days return karo (agar overlap nahi hai toh 0)
        return max(0, end_together - start_together + 1)
