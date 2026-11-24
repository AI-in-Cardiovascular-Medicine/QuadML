**Dimensionality Reduction** compresses features **after** Feature Selection. **None** leaves the selected columns unchanged. FS × DR combinations are searched together.

## Methods

| Method | What it does | When to use it |
|--------|--------------|----------------|
| **None** | No projection | Default first choice |
| **PCA** | Linear principal components | Correlate/compress numeric features |
| **ICA** | Independent components | Separating mixed signals |
| **Kernel PCA** | Nonlinear components | Nonlinear structure |
| **LDA** | Supervised linear discriminants | **Classification only** |

**Point:** Keep **None** unless you already know you want components. After DR, Interpretability refers to components, not original names.
