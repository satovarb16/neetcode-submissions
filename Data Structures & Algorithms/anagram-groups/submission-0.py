class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #creamos un array tamano 26 todo en 0. Y un hash
        hashmap = {}
        #iteramos cada palabra de la lista, y agregamos respectivamente +1 al array tamano 26 dependiendo la letra
        for word in strs:
            freq = [0]*26
            for letter in word:
                indx = ord(letter) - ord('a')
                freq[indx] += 1
        #convertimos en touple
            key = tuple(freq)
        #agregamos al hash como frecuencia : palabra
        #si la frecuencia ya existe, agregamos directamente la palabra como value de esa key. 
        #retornamos valores
            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key] = [word]
        return list(hashmap.values())
        