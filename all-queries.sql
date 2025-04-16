-- Five country consultation

SELECT 
    country_first_import_name AS pais, 
    SUM(fob_usd) AS valor_total_importacao
FROM basedosdados.br_trase_supply_chain.beef
WHERE 
    year = (SELECT MAX(year) FROM basedosdados.br_trase_supply_chain.beef)
GROUP BY country_first_import_name
ORDER BY valor_total_importacao DESC
LIMIT 5;

-- Exports over one million

SELECT 
    municipality_id_production AS municipio, 
    SUM(fob_usd) AS valor_total_exportacao
FROM basedosdados.br_trase_supply_chain.beef
WHERE 
    year = (SELECT MAX(year) FROM basedosdados.br_trase_supply_chain.beef) AND
    fob_usd > 0
GROUP BY municipality_id_production
HAVING SUM(fob_usd) > 1000000
ORDER BY valor_total_exportacao DESC;