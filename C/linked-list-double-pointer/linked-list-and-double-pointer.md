# 链表与二级指针

## 一、链表基础

### 1. 什么是链表

链表（Linked List）是一种线性的数据结构，由一个个**节点（Node）**串联而成。每个节点包含两部分：

- **数据域**：存放实际数据（如 `int val`）
- **指针域**：存放下一个节点的地址（`struct node *next`）

节点之间通过指针连接，形成一条"链"。链表的入口是**头指针** `head`，它指向第一个节点；最后一个节点的 `next` 指向 `NULL`，表示链表结束。

```text
head
  |
  v
+-------+    +-------+    +-------+
| 1 | --+--> | 2 | --+--> | 3 | --+--> NULL
+-------+    +-------+    +-------+
```

### 2. 节点结构

```c
typedef struct node {
    int val;            /* 数据域：存放数据 */
    struct node *next;  /* 指针域：指向下一个节点 */
} Node;
```

### 3. 链表 vs 数组

| 特性 | 数组 | 链表 |
|------|------|------|
| 内存 | 连续分配 | 分散分配，靠指针连接 |
| 随机访问 | O(1)，下标直接访问 | O(n)，需从头遍历 |
| 插入/删除 | 需移动元素 O(n) | O(1)（找到位置后只改指针） |
| 扩容 | 需整体重新分配 | 按需动态添加节点 |

---

## 二、指针与二级指针

### 1. 一级指针回顾

指针是一个变量，它存储的是**另一个变量的地址**。

```c
int a = 10;
int *p = &a;   /* p 存储 a 的地址 */
*p = 20;       /* 通过 *p 解引用，修改 a 的值 */
```

- `&a`：取变量 `a` 的地址
- `*p`：解引用，通过 p 中存的地址访问/修改原变量

### 2. 什么是二级指针

二级指针是一个**指向指针的指针**，它存储的是"指针变量的地址"。

```c
int a = 10;
int *p = &a;    /* 一级指针 p 指向 a */
int **pp = &p;  /* 二级指针 pp 指向 p */
```

```text
 pp        p         a
+---+    +---+     +----+
| &p |--> | &a |--> | 10 |
+---+    +---+     +----+
```

- `pp`  存的是 `p` 的地址
- `*pp` 等价于 `p`（得到 p 的值，即 a 的地址）
- `**pp` 等价于 `*p`，最终得到数据 `a`

### 3. 为什么链表需要二级指针

这是理解二级指针写链表的关键。先记住一个原则：

> **当函数要修改"指针变量本身"时，就必须传二级指针（指针变量的地址）。**

链表操作中，哪些情况需要修改头指针 `head` 本身？

- **头部插入**：`head` 要从指向旧头节点，改为指向新节点。
- **删除头节点**：`head` 要从指向头节点，改为指向第二个节点。

`head` 本身是一个**指针变量**。函数要修改它，就必须拿到它的**地址**，也就是 `Node **`（指向指针的指针）。

如果只用一级指针会怎样？看下面的错误示范：

```c
/* 错误：一级指针无法真正修改调用者的 head */
void push_front_wrong(Node *head, int val) {
    Node *n = (Node *)malloc(sizeof(Node));
    n->val = val;
    n->next = head;
    head = n;   /* 只修改了局部变量 head，调用者的 head 不变！ */
}
```

这里 `head` 是函数参数（一份拷贝的局部变量），对它赋值只改变了这份副本，**调用者的 `head` 仍然是旧值**，函数返回后新节点就"丢失"了。

因此，凡是可能改变头指针的操作，参数都应该传 `Node **head`，调用时用 `&head`。

---

## 三、用二级指针实现链表

### 1. 核心思想：用 Node **pp 统一处理

二级指针写链表最优雅的地方在于：用 `Node **pp` 来遍历，让 `pp` 始终指向**"指向当前节点的指针"**。这样删除节点时，无论是头节点还是中间节点，都只需要一句：

```c
*pp = cur->next;   /* 让"指向 cur 的指针"直接跳过 cur，指向下一个 */
```

- **删除头节点**：`pp` 指向 `head` 本身，`*pp = cur->next` 等价于 `head = cur->next`。
- **删除中间节点**：`pp` 指向前一个节点的 `next` 域，`*pp = cur->next` 等价于 `prev->next = cur->next`。

两种情况代码完全一致，**无需为头节点写特殊分支**。这正是 Linus Torvalds 强调的"好品味"（good taste）——消除边界情况的特殊处理。

### 2. 头部插入 push_front

```c
void push_front(Node **head, int val) {
    Node *n = (Node *)malloc(sizeof(Node));
    if (!n) return;
    n->val = val;
    n->next = *head;   /* 新节点指向原头节点 */
    *head = n;         /* 头指针指向新节点 */
}
```

### 3. 删除节点 delete_by_value

```c
void delete_by_value(Node **head, int val) {
    Node **pp = head;          /* pp 指向"指向当前节点的指针" */
    while (*pp != NULL) {
        Node *cur = *pp;
        if (cur->val == val) {
            *pp = cur->next;   /* 让上一个指针直接跳过 cur */
            free(cur);
            return;
        }
        pp = &cur->next;       /* pp 前进到下一个指针域 */
    }
}
```

逐步分析删除过程：

```text
初始:  pp -> head -> [1] -> [2] -> [3] -> NULL

第一轮: cur = *pp = [1]，值不等于目标
        pp = &cur->next    （pp 现在指向 [1] 的 next 域）

第二轮: cur = *pp = [2]，值等于目标
        执行 *pp = cur->next
        即 [1] 的 next 域 直接指向 [3]，[2] 被 free
        结果: pp -> [1].next -> [3]
```

### 4. 销毁链表 destroy

```c
void destroy(Node **head) {
    Node *cur = *head;
    while (cur != NULL) {
        Node *next = cur->next;
        free(cur);
        cur = next;
    }
    *head = NULL;   /* 防止悬空指针 */
}
```

---

## 四、用一级指针写链表（对比）

### 1. 一级指针的头部插入

一级指针无法直接修改调用者的 `head`，所以头部插入只能**返回新的头指针**，让调用方接收：

```c
Node *push_front(Node *head, int val) {
    Node *n = (Node *)malloc(sizeof(Node));
    if (!n) return head;
    n->val = val;
    n->next = head;
    return n;   /* 必须把新头返回给调用者 */
}
```

调用时必须写 `head = push_front(head, 3);`，如果忘记接收返回值，新节点就会丢失。

### 2. 一级指针的删除节点

用一级指针删除节点，最大的痛点是**头节点需要单独处理**，中间节点还要额外用一个 `prev` 指针跟踪前驱：

```c
Node *delete_by_value(Node *head, int val) {
    /* 情况1：删除的是头节点，必须单独判断 */
    if (head != NULL && head->val == val) {
        Node *tmp = head;
        head = head->next;
        free(tmp);
        return head;   /* 返回新头 */
    }

    /* 情况2：删除中间/尾节点，用 prev 跟踪前一个节点 */
    Node *prev = NULL;
    Node *cur = head;
    while (cur != NULL) {
        if (cur->val == val) {
            prev->next = cur->next;
            free(cur);
            break;
        }
        prev = cur;
        cur = cur->next;
    }
    return head;   /* 头没变，原样返回 */
}
```

一级指针版本的调用方式：

```c
Node *head = NULL;
head = push_front(head, 3);      /* 每次都要 head = 接收 */
head = push_front(head, 2);
head = push_front(head, 1);
head = delete_by_value(head, 2); /* 删头节点也要 head = 接收 */
head = delete_by_value(head, 1);
```

### 3. 一级指针 vs 二级指针 对比

| 对比项 | 一级指针 | 二级指针 |
|--------|---------|---------|
| 修改头指针 | 靠返回值，调用方须 `head = ...` | 直接改 `*head` |
| 删除头节点 | 需写单独分支 | 与中间节点统一处理 |
| 删除中间节点 | 需 `prev` 跟踪前驱 | 用 `**pp` 定位"前驱的 next 域" |
| 出错风险 | 易忘记 `head =` 接收返回值 | 编译器可检查类型，更安全 |
| 代码量 | 分支多、有重复 | 更简洁、无边界分支 |

**结论**：一级指针版本需要「返回新头 + 头节点特殊处理 + prev 跟踪」三处额外负担；而二级指针版本通过 `Node **` 把这些统一成一句 `*pp = cur->next`，代码更简洁，也杜绝了"忘记接收返回值"的隐患。

---

## 五、完整示例代码

完整可运行的代码见同目录下的 `list.c`，可直接编译运行：

```bash
gcc list.c -o list && ./list
```

运行结果：

```text
插入 1,2,3 后:   1 -> 2 -> 3 -> NULL
删除 2 后:      1 -> 3 -> NULL
删除头节点 1 后: 3 -> NULL
删除 99 后:     3 -> NULL
销毁后 head = (nil)
```

---

## 六、小结

1. **指针**存的是"变量的地址"，**二级指针**存的是"指针变量的地址"。
2. 链表操作只要**可能修改头指针本身**（头插、删头节点），就要传二级指针 `Node **head`。
3. 用 `Node **pp` 遍历链表，可以让"删头节点"和"删中间节点"共用同一套代码，消除边界特殊处理。
4. 完整代码见 `list.c`，编译运行：`gcc list.c -o list && ./list`

