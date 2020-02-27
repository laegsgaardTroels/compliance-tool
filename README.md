# Data

Data used to search for suspicious entities.

## OFAC Sanctions

The Office of Foreign Assets Control (OFAC) of the US Department of the Treasury administers and enforces economic and trade sanctions based on US foreign policy and national security goals against targeted foreign countries and regimes, terrorists, international narcotics traffickers, those engaged in activities related to the proliferation of weapons of mass destruction, and other threats to the national security, foreign policy or economy of the United States. OFAC acts under Presidential national emergency powers, as well as authority granted by specific legislation, to impose controls on transactions and freeze assets under US jurisdiction. Many of the sanctions are based on United Nations and other international mandates, are multilateral in scope, and involve close cooperation with allied governments. 

#### Source

    [1] https://www.treasury.gov/resource-center/sanctions/SDN-List/Pages/consolidated.aspx

## ICIJ

This database contains information on more than 785,000 offshore entities that are part of the Paradise Papers, the Panama Papers, the Offshore Leaks and the Bahamas Leaks investigations. The data links to people and companies in more than 200 countries and territories.


#### Source

The source of this data is data from a graphical Neo4j database freely available. 

    [1] https://offshoreleaks.icij.org/pages/database

## Finanstilsynet
 
The file `Finanstilsynets virksomhedsregister - SQL.xlsx` contains everything from this source.

Registret indeholder oplysninger om de virksomheder, som Finanstilsynet har under tilsyn samt virksomheder, som Finanstilsynet har givet tilladelse eller notifikation til at drive finansiel virksomhed i Danmark.

#### Source

    [1] https://www.finanstilsynet.dk/Tilsyn/Virksomheder-under-tilsyn/Finanstilsynets-virksomhedsregister

## CVR Register

#### Source

[1] does not require a token but [2] does.

    [1] http://datahub.virk.dk/dataset/system-til-system-adgang-til-regnskabsdata
    [2] http://datahub.virk.dk/dataset/system-til-system-adgang-til-cvr-data


## Companies House

Companies House is Great Britains CVR register. They have endpoints for downloading data in [1] and you can download a zip at [2]. An analysis of the data in [2] is found in [4]. Accounts data is available at [3].

#### Source

    [1] https://www.gov.uk/government/organisations/companies-house/about-our-services#uri-info
    [2] http://download.companieshouse.gov.uk/en_output.html
    [3] http://download.companieshouse.gov.uk/en_accountsdata.html
    [4] https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/2662301365741150/901133009736515/4813839007128744/latest.html
