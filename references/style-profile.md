# Strict design and editing profile

The user selected this profile for his own coursework text. Apply it when writing and editing every chapter, table and conclusion. This is a preference for design and quality, not a list of evidence of machine authorship. The sources reviewed do not establish a universal list of such evidence; Do not promise the result of the detector or the indistinguishability of text from human text.

## Symbols prohibited in the author’s own prose

| Element | Rule and replacement |
|---|---|
| Em dash, en dash and horizontal dash, U+2012, U+2013, U+2014, U+2015 | Do not use it as author's punctuation. Rearrange the sentence: period, comma, colon, parentheses or explicit verb according to the meaning. The range in the author's phrase can be written with the words “from ... to ...”, substituting real values. |
| Ellipsis U+2026 and three or more dots in a row | Do not use for understatement, intrigue, reinforcement or vague continuation. Formulate a complete thought. |
| Emoji, pictograms, checkmarks, stars, diamonds, triangles, decorative markers | Put away the decorations. For this listing, use simple numbering or design according to the manual. |
| Arrows and graphic links instead of explanation | In the author's argument, describe the relationship with words: cause, effect, stage or dependence. Scientific notations are discussed separately below. |
| Invisible inserts, zero-width, internal BOM, soft hyphens and directional symbols | Do not add them to the Russian author's prose. When importing, check the origin and function; Don't automatically call them AI watermarks. |
| Service reference tokens, turnNsearchN, oaicite and contentReference | Don't leave them in your coursework. Replace with a full verified link and bibliographic entry. |

Keep the usual hyphen in compound words. Do not replace any dash with a hyphen mechanically: this may spoil the syntax. In your own text, rewrite the entire construction. Do not insert invisible characters or similar letters from another alphabet to bypass the check.

## Templates prohibited as filler

In the new author’s prose, do not use empty introductions “in the modern world”, “in our time”, “today”, “in a rapidly changing world”. Be specific about the subject, period, and problem. Preserve historical titles or analyzed quotations containing such words.

Remove unnecessary thought declarations: “should be noted”, “worth noting”, “important to emphasize”, “cannot be ignored”, “must be understood”, “important to remember”. Immediately formulate the thesis itself with its proof.

Unsupported amplifiers and ratings are prohibited: “certainly”, “undoubtedly”, “indisputable”, “obviously”, “indisputable”, “unique”, “revolutionary”, “tremendous”, “key role”, “invaluable contribution”, “significant impact”. Name a specific effect, criterion or result of the source. Don't make up a number to replace an evaluative word.

Do not use conversation with the reader inside the coursework: “let’s take a look,” “let’s dive in,” “we’ll figure it out together,” “I hope this helps,” “if you have any questions.” Don’t insert the model’s self-presentation: “like an AI,” “like a language model,” “I can’t have an opinion.” Give honest communication about the limitations of the environment separately from the academic text.

Vapid rhetorical juxtapositions of “it’s not just X, it’s Y,” artificial triplets of epithets, advertising metaphors, and general praise of relevance are prohibited. Save and support the actual comparison of definitions, results and methods with sources.

Do not replace analysis with lists, identical paragraphs based on a template, and repetition of one thought with synonyms. Don't end each paragraph with "thus" or "to summarize." The summary of the chapter should meet the task and summarize the results, and not repeat its introduction. Normal connectives “however”, “therefore” and “thus” are acceptable when they express a real logical connection; There is no general ban on Russian grammar.

English lists like delve, tapestry, landscape and pivotal are not a proven Russian dictionary of features. Do not borrow these words or their literal translations for the sake of decorating the text. Save the required term, surname and real title of the publication exactly.

## Design according to the requested format

Without decorative dividers, subheadings for each paragraph, obsessive bolding and lists instead of coherent reasoning. In plain text and DOCX, don't leave raw Markdown characters and backticks around regular terms. If Markdown is requested, its headers and tables are the output format and are saved; In DOCX, use real styles, not markup characters. Don't prohibit a list or table that is actually needed for the assignment.

Do not remove normal quotation marks, "e", number signs, percentages, decimal points, references [1], parentheses, Greek letters, mathematical minus signs, and normal non-breaking spaces simply because of their appearance. They do not serve as proof of authorship.

## Accuracy and justified exceptions

Save verbatim citations, official names, DOI/URL, bibliographic details, code, formulas, chemical reactions, mathematical sequences and necessary symbols in the analyzed data. For example, a reaction arrow, a minus sign, or an ellipsis in a mathematical sequence have meaning. Don't ruin them to suit their appearance. If quoting the original sentence is not necessary, you can replace the quotation with your own correct paraphrase with reference, but you cannot discreetly change a verbatim quotation.

If an explicitly specified manual requires a certain sign or marking, note the conflict with the profile. Fulfill the explicit design requirement as a specific exception and document it in the accompanying report. Scientific accuracy and reliable details are not replaced by cosmetics.

## Check before issue

1. Check your own text for prohibited characters, service artifacts and empty templates. Rewrite the violations according to their meaning.
2. If Python and the script itself are available, export the version you are checking in UTF-8 and run from the skill folder:

       python scripts/check_style.py path/to/draft.md --json

   If the python command is not available, use the discovered Python executable. The script reads the text and does not change the file. Returning 0 means no finds in the checked rows, 1 means no finds, 2 means an input error. This is a character scanner, not an AI detector or content checker.
3. For an immutable citation, bibliography, or scholarly record, you can explicitly specify physical lines: --allow-lines 12:14. Check the reason for each exception and indicate it in the report. The author's paragraph cannot be excluded to hide the violation. For a mixed string, check the author part manually or export it separately for scanning.
4. Check rhetoric and repetition manually: the script does not determine the meaning, emptiness of a phrase, the correctness of Markdown or the quality of the argument.
5. Provide Luna with the reasons for the exceptions and the modified statements. If an edit has changed the meaning, number, source, or scope of the output, repeat the appropriate audit. A simple symbol check does not give the “sources verified” status.

Without tools, do an explicit manual check and don't claim the script ran. Maintain the same requirements for independent audit and draft status.

## Foundations and limits

Frequency changes in the English academic dictionary are described in [Kobak et al., arXiv:2406.07016v3](https://arxiv.org/html/2406.07016v3). A small Russian-language qualitative study notes repetition and stereotypes: [Gorina and Ufimtseva, 2024](https://rulb.org/archive/1-49-2024-january/10.18454/RULB.2024.49.27). These works do not prove that the listed Russian phrases or symbols establish the origin of a particular coursework.

Empirical limitations of the detectors are shown in [Liang et al.](https://arxiv.org/abs/2304.02819) and [Sadasivan et al.](https://arxiv.org/abs/2303.11156). The academic publishing guide itself uses dashes and ellipses: [Harvard Law School Editorial Style Guide](https://hls.harvard.edu/communications-office/hls-style-guides/editorial-style-guide/). Prohibiting these marks in your own presentation here is a user choice, not a set AI feature.
