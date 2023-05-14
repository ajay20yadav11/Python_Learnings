class OmniCreate:
    def MxN_Matrix(self, m, n, current_m, current_n):
        if current_m == m - 1 or current_n == n - 1:
            return 1

        total_track = self.MxN_Matrix(m, n, current_m + 1, current_n) + self.MxN_Matrix(
            m, n, current_m, current_n + 1
        )

        return total_track


create = OmniCreate()

print(create.MxN_Matrix(8, 8, 0, 0))
