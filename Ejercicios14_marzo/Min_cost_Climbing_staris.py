class Solution:
    def minCostClimbingStairs(self, costos: list[int]) -> int:
        """
        Estrategia DP:
        dp[i] = costo mínimo para llegar al escalón i.

        Recurrencia:
        dp[i] = costos[i] + min(dp[i-1], dp[i-2])

        Caso base:
        dp[0] = costos[0]
        dp[1] = costos[1]

        Complejidad:
        Tiempo: O(n)
        Espacio: O(1)
        """

        costo_dos_atras = costos[0]
        costo_uno_atras = costos[1]

        for i in range(2, len(costos)):

            costo_actual = costos[i] + min(
                costo_uno_atras,
                costo_dos_atras
            )

            costo_dos_atras = costo_uno_atras
            costo_uno_atras = costo_actual

        return min(costo_uno_atras, costo_dos_atras)