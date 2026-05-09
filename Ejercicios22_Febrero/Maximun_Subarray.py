class Solution:
    def maxSubArray(self, numeros: list[int]) -> int:
        """
        Estrategia DP (Kadane):
        dp[i] = suma máxima de subarreglo que termina en i.

        Recurrencia:
        dp[i] = max(numeros[i], dp[i-1] + numeros[i])

        Complejidad:
        Tiempo: O(n)
        Espacio: O(1)
        """

        suma_actual = numeros[0]
        suma_maxima = numeros[0]

        for i in range(1, len(numeros)):
            numero = numeros[i]

            # decidir si continuar o empezar nuevo subarreglo
            suma_actual = max(numero, suma_actual + numero)

            # actualizar mejor resultado global
            suma_maxima = max(suma_maxima, suma_actual)

        return suma_maxima