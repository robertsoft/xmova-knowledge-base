# Regex Blocks Report
Total samples scanned: 200

## Block counts
- **views**: 15
- **recorddetail**: 1

## Example block (first)
- file: 130123410--130123410_src_app_screens--ResumoApontamentoDetail.xmv
- type: views

```
	views
		recordList getRecords=_resumoApontamento
			recordDetail fields=tipoApontamento,descricao,dataInicial,dataFinal,duracao labels
		recordList getRecords=_resumoTotal
			recordDetail fields=duracaoServico,duracaoParada,duracaoDeslocamento labels
	events
		beforeInit
			_resumoApontamento = Select * FROM ResumoApontamento
			_resumoTotal = Select * FROM ResumoTotal
		beforeClose
			_resumoApontamento = null
			_resumoTotal = null
```