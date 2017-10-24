tree = [None]*(10**6 + 1)
A = [None]*(10**6 + 1)
lazy = [None]*(10**6 + 1)

def build(node, start, end):
    if start==end:
        tree[node] = A[start]
    else:
        mid = int(start + (end-start)/2)
        build(2*node, start, mid)
        build(2*node+1, mid+1, end)
        tree[node] = tree[2*node] + tree[2*node+1]
        
def update(node, start, end, idx, val):
    if start==end:
        A[idx] += val
        tree[node] += val
    else:
        mid = int(start + (end-start)/2)
        if start <= idx and idx <= mid:
            update(2*node, start, mid, idx, val)
        else:
            update(2*node+1, mid+1, end, idx, val)
        tree[node] = tree[2*node] + tree[2*node+1]
        
def updateRange(node, start, end, l, r, val):
    if start > end or start > r or end < l:
        return

    if start == end:
        tree[node] += val
        return

    mid = int(start + (end-start)/2)
    updateRange(node*2, start, mid, l, r, val)
    updateRange(node*2 + 1, mid + 1, end, l, r, val)

    tree[node] = tree[node*2] + tree[node*2+1]
    
def updateRange(node, start, end, l, r, val):
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]           
        lazy[node] = 0

    if start > end or start > r or end < l:
        return
    
    if start >= l and end <= r:
        tree[node] += (end - start + 1) * val
        if start != end:
            lazy[node*2] += val
            lazy[node*2+1] += val
        return
    
    mid = (start + end) / 2
    updateRange(node*2, start, mid, l, r, val)
    updateRange(node*2 + 1, mid + 1, end, l, r, val)
    tree[node] = tree[node*2] + tree[node*2+1]

def queryRange(node, start, end, l, r):
    if start > end or start > r or end < l:
        return 0
        
    if lazy[node] != 0:
        tree[node] += (end - start + 1) * lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0
    
    if start >= l and end <= r:
        return tree[node]
    mid = (start + end) / 2
    p1 = queryRange(node*2, start, mid, l, r)
    p2 = queryRange(node*2 + 1, mid + 1, end, l, r)
    return (p1 + p2)

def query(node, start, end, l, r):
    if r < start or end < l:
        return 0
    if l <= start and end <= r:
        return tree[node]
    mid = int(start + (end-start)/2)
    p1 = query(2*node, start, mid, l, r)
    p2 = query(2*node+1, mid+1, end, l, r)
    return (p1 + p2)
    
