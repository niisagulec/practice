# ListNode sınıfı, tek yönlü bağlı listenin her bir düğümünü temsil eder
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val      # Bu düğümdeki değer
        self.next = next    # Bir sonraki düğüme bağlantı

# İki bağlı listeyi toplayan çözüm sınıfı
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # Sahte (dummy) başlangıç düğümü oluştur
        dummy = ListNode(0)
        current = dummy   # Sonuç listesi üzerinde hareket eden gösterici
        carry = 0         # Elde (taşıma) değeri

        # Her iki liste de bitene kadar veya elde varsa döngü devam eder
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0   # l1 varsa değerini al, yoksa 0
            val2 = l2.val if l2 else 0   # l2 varsa değerini al, yoksa 0

            total = val1 + val2 + carry  # Toplamı hesapla
            carry = total // 10          # Yeni elde değeri
            new_digit = total % 10       # Yeni rakamı belirle

            # Yeni node oluştur ve bağlı listeye ekle
            current.next = ListNode(new_digit)
            current = current.next       # Bir sonraki düğüme geç

            # l1 ve l2'yi ilerlet (varsa)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  # Sonuç listesinin başı (dummy sonrası)

# Yardımcı fonksiyon: Python listesini bağlı listeye çevirir
def list_to_nodes(lst):
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Yardımcı fonksiyon: Bağlı listeyi ekrana yazdırır
def print_nodes(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Örnek veri: [2,4,3] + [5,6,4] = [7,0,8]
l1 = list_to_nodes([2, 4, 3])  # 342
l2 = list_to_nodes([5, 6, 4])  # 465

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Sonucu yazdır
print("Sonuç:")
print_nodes(result)
