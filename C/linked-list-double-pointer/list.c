#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int val;
    struct node *next;
} Node;

/* 头部插入：因为要修改 head 本身，参数用二级指针 */
void push_front(Node **head, int val) {
    Node *n = (Node *)malloc(sizeof(Node));
    if (!n) return;
    n->val = val;
    n->next = *head;   /* 新节点指向原头节点 */
    *head = n;         /* head 指向新节点 */
}

/* 删除指定值的节点：用二级指针遍历，头/中间节点统一处理 */
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

/* 遍历打印 */
void print_list(Node *head) {
    Node *p;
    for (p = head; p != NULL; p = p->next)
        printf("%d -> ", p->val);
    printf("NULL\n");
}

/* 销毁整个链表 */
void destroy(Node **head) {
    Node *cur = *head;
    while (cur != NULL) {
        Node *next = cur->next;
        free(cur);
        cur = next;
    }
    *head = NULL;   /* 防止悬空指针 */
}

int main(void) {
    Node *head = NULL;

    push_front(&head, 3);
    push_front(&head, 2);
    push_front(&head, 1);
    printf("插入 1,2,3 后:   ");
    print_list(head);

    delete_by_value(&head, 2);
    printf("删除 2 后:      ");
    print_list(head);

    delete_by_value(&head, 1);   /* 删除头节点，无需特殊处理 */
    printf("删除头节点 1 后: ");
    print_list(head);

    delete_by_value(&head, 99);  /* 删除不存在的值，无副作用 */
    printf("删除 99 后:     ");
    print_list(head);

    destroy(&head);
    printf("销毁后 head = %p\n", (void *)head);
    return 0;
}
