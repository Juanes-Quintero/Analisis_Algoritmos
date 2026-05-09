class Solution:
    def rob(self, numeros: list[int]) -> int:
        """
        Estrategia DP:
        dp[i] = máximo dinero que puedo robar hasta la casa i.

        Recurrencia:
        dp[i] = max(
            dp[i-1],
            dp[i-2] + numeros[i]
        )

        Caso base:
        dp[0] = numeros[0]
        dp[1] = max(numeros[0], numeros[1])

        Complejidad:
        Tiempo: O(n)
        Espacio: O(1)
        """

        if len(numeros) == 1:
            return numeros[0]

        anterior_dos = numeros[0]
        anterior_uno = max(numeros[0], numeros[1])

        for i in range(2, len(numeros)):

            mejor_actual = max(
                anterior_uno,
                anterior_dos + numeros[i]
            )

            anterior_dos = anterior_uno
            anterior_uno = mejor_actual

        return anterior_uno