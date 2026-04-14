<!-- Absorbed from skills/paper-compile/SKILL.md -->

# Paper Compile: LaTeX to PDF

Compile the statistics paper to PDF from: **$ARGUMENTS**

## Prerequisites

Check that LaTeX tools are available:
```bash
which pdflatex && which bibtex && which latexmk
```

If not installed, advise the user:
- macOS: `brew install --cask mactex` or `brew install basictex`
- Linux: `sudo apt-get install texlive-full`

## Workflow

### Step 1: Locate Main File

Find the main .tex file:
1. Use argument if provided
2. Check `paper/main.tex`
3. Search for `\documentclass` in .tex files

### Step 2: Pre-Compilation Checks

Before compiling:
1. **Check all `\input{}` files exist**: Parse main.tex for includes
2. **Check all figure files exist**: Parse for `\includegraphics`
3. **Check .bib file exists**: Parse for `\bibliography`
4. **Check for `[VERIFY]` markers**: Flag unresolved citations
5. **Check style file**: Ensure venue-specific .sty/.cls files are present

### Step 3: Compile

```bash
cd paper/ && latexmk -pdf -interaction=nonstopmode main.tex 2>&1 | tee compile.log
```

### Step 4: Error Diagnosis and Auto-Fix

If compilation fails, diagnose and fix (up to 3 iterations):

| Error Pattern | Fix |
|--------------|-----|
| `Undefined control sequence` | Add missing package or define command |
| `Missing $ inserted` | Fix math mode delimiters |
| `File not found` | Check path, fix `\input` or `\includegraphics` |
| `Citation undefined` | Run bibtex, check .bib entries |
| `Misplaced alignment tab` | Fix table `&` alignment |
| `Environment undefined` | Add `\newtheorem` or load package (amsthm) |
| `Too many unprocessed floats` | Add `\clearpage` or adjust float placement |
| `Font shape not available` | Install missing fonts or substitute |

After each fix, recompile and check.

### Step 5: Post-Compilation Checks

After successful compilation:

1. **Page count**: Check manuscript length against venue requirements
2. **Figures rendered**: Verify all figures appear correctly
3. **Tables formatted**: Check alignment and readability
4. **References**: Verify bibliography rendered (no `[?]` citations)
5. **Theorem numbering**: Check sequential and consistent
6. **Cross-references**: No `??` from unresolved `\ref`
7. **Stale files**: Check if any .aux files are outdated
8. **`[VERIFY]` markers**: Report any remaining in the PDF

### Step 6: Report

```markdown
## Compilation Report

- **Status**: SUCCESS / FAILED
- **PDF**: paper/main.pdf
- **Pages**: X (target: Y for [VENUE])
- **Warnings**: [list any LaTeX warnings]
- **Unresolved references**: [list any ?? or [?]]
- **[VERIFY] markers remaining**: [count]
- **Errors fixed**: [list auto-fixes applied]
```

## Key Rules

- Always use `latexmk -pdf` for reliable multi-pass compilation
- Run bibtex/biber as needed for bibliography
- Don't suppress warnings — they often indicate real issues
- Check for orphaned figures (included but not referenced in text)
- Verify theorem environments are properly defined
- For statistics papers: ensure amsthm is loaded for theorem environments
