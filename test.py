# Vectors
vec_a = [1, 2, 3, 4, 5]
vec_b = [1, 3, 5, 7, 9]

# Dot and norm
dot = sum(a*b for a, b in zip(vec_a, vec_b))
norm_a = sum(a*a for a in vec_a) ** 0.5
norm_b = sum(b*b for b in vec_b) ** 0.5

# Cosine similarity
cos_sim = dot / (norm_a*norm_b)
