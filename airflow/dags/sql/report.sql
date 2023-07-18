WITH merged_data AS (
    SELECT w.product, m.id, m.val, w.production
    FROM public.workorders w
    JOIN public.metrics m ON w.time = m.time
    WHERE m.val IS NOT NULL AND w.production IS NOT NULL
)
, correlation AS (
    SELECT product, id, abs(CORR(val, production)) AS correlation
    FROM merged_data
    GROUP BY product, id
)
, ranked_data AS (
    SELECT
        product,
        id,
        correlation,
        row_number() over (partition by product order by correlation DESC) as rank
    FROM correlation
    WHERE correlation IS NOT NULL
)
SELECT product, id
FROM ranked_data rd
WHERE rank <= 3
GROUP BY 1, 2
;