![IATI Plus Logo](https://github.com/Donator-ai/Development-Lab/blob/main/Media/iatiplus_db2.png)

For the benefit of the humanitarian community, volunteers from Donator's **Development Lab** are working with members of the **Partnership on Generative AI for Humanitarian Applications** and others on developing a hybrid **IATI database** geared specifically for powering sophisticated new humanitarian AI applications operating at scale. The database is called **IATI Plus**.

## Data Source

**IATI** is an XML standard and open data sharing framework widely used across the humanitarian community that is managed by the [Internatioinal Aid Transparency Initiative](https://iatistandard.org/en/). Currently, over 1700 organizations are channeling information on aid activities, transactions and results through the framework. **IATI Plus** is a fully up-to-date, graphed version of IATI's entire corpus which contains information on over 900,000 activities.

## Architecture

![IATI Graph](https://github.com/Donator-ai/Development-Lab/blob/main/Media/IATI_IATIPlus.png)

IATI data is highly structured making IATI an ideal data source for machine applications. However IATI data is challenging to flatted due to its nested structure and IATI's XML Standard contains hundreds of information fields, making IATI's vast corpus and the data's cross-connecting relationships challegning to traverse. Graphing IATI data can facilitate complex query navigation. IATI Plus is a graphed version of IATI but an extensible version capable of handling experimental non-standard information fields.

## Layering

IATI Plus isn't designed to replace IATI. The database can be compared to a Geographic Information System (GIS). It is a clone that works like an identical overlayer, but a robust one geared to me queried by consumer grade applications operating at scale and in more complex ways than IATI can be traversed. 

## Benefits

Because users can also write to IATI Plus, the database can be used to draft, pre-publish, share and traverse aid activity files prior to formally publishing files to IATI. This makes it possilbe for teams to collaborate on generating files and even privately share files across organizations prior to pulblishing and execute query tests on all of the information. Using IATI plus users can also virtually publish to IATI while keeping all or a portion of their information private.

## Donator

Donator uses IATI as a data source and as a workspace. Once ready, users can use Donator to publish to IATI, populating both IATI and IATI Plus' underlayer.
