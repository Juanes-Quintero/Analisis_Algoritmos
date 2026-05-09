class Solution:
    def twoSum(self, numeros: list[int], objetivo: int) -> list[int]:
        """
        Estrategia:
        Usar un diccionario para guardar valores ya vistos.

        Idea:
        Para cada número, buscar si ya existe su complemento:
        complemento = objetivo - numero

        Complejidad:
        Tiempo: O(n)
        Espacio: O(n)
        """

        indices_por_valor = {}  # valor -> índice

        for indice_actual, numero in enumerate(numeros):

            complemento = objetivo - numero

            # Verificar si ya vimos el complemento
            if complemento in indices_por_valor:
                return [indices_por_valor[complemento], indice_actual]

            # Guardar el número actual
            indices_por_valor[numero] = indice_actual