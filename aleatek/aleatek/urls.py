from django.contrib import admin
from django.urls import path, include
from .views import get_csrf_token
from clients.views import ClientViewsetAdmin
from Media.views import MediaSerializerAdmin
# from affaires.views import PlanAffaireAdminViewsetAdmin
from constructeurs.views import EntrepriseAdminViewsetAdmin, MediaEntrepriseAdminViewsetAdmin
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from marques.views import MarqueAdminViewsetAdmin

from IT.views import InterventionTechniqueAdminViewsetAdmin, PrestationAssocieAdminViewsetAdmin

from missions.views import MissionsAdminViewsetAdmin

from services.views import CbAdminViewsetAdmin

from collaborateurs.views import CollaborateursAdminViewsetAdmin, UtilisateursConnectes

from destinations.views import DestinationBatimentAdminViewsetAdmin

from Dashbord.views import ProductAdminViewsetAdmin, FicheAffairesAdminViewsetAdmin, \
    PlanAffairesAdminViewsetAdmin, FilterQuerysetAdminView, TableauDeBordQuerysetAdminView, FilterQuerysetAffaireDocumentAdminView

from destinations.views import DestinationBatimentAdminViewsetAdmin
from Document.views import AvisAdminViewset, DocumentsAdminViewsetAdmin, FichierAdminViewsetAdmin, AffectaionInterventionAdminViewsetAdmin, CommentaireAvisAdminViewsetAdmin
from Aso.views import AsoAdminViewsetAdmin
from Ouvrages.views import OuvagesDiffusionAdminViewsetAdmin, AvisSurOuvragesAdminViewsetAdmin, OuvagesAdminViewset
from Rapports.views import StatutSaisiRapportAdminViewsetAdmin, AIEAdminViewsetAdmin, RapportDeConceptionViewsetAdmin,\
    RapportDeVisiteViewsetAdmin


# Ici nous créons notre routeur
router = routers.SimpleRouter()
#router.register('admin/users/connected/<int:id>',UtilisateursConnectes, basename='admin-connexion')
router.register('admin/document/filter',FilterQuerysetAffaireDocumentAdminView, basename='admin-documentfilter')
router.register('admin/commentaire/avis' ,CommentaireAvisAdminViewsetAdmin, basename='admin-commentaire-avis')
router.register('admin/intervenant',AffectaionInterventionAdminViewsetAdmin, basename='admin-intervanant')
router.register('admin/rapport/visite', RapportDeVisiteViewsetAdmin, basename='admin-rapport')

router.register('admin/prestation/associe', PrestationAssocieAdminViewsetAdmin, basename='admin-prestation')

#prestatio Associé
router.register('admin/rapport/conception', RapportDeConceptionViewsetAdmin, basename='admin-rapportdeconception')
router.register('admin/aie', AIEAdminViewsetAdmin, basename='admin-aie')
router.register('admin/statut/saisie/rapport', StatutSaisiRapportAdminViewsetAdmin, basename='admin-statt-rapport')
#les routes relatives aux rapport
router.register('admin/aso', AsoAdminViewsetAdmin, basename='amin-aso')
router.register('admin/ouvrage/diffusion', OuvagesDiffusionAdminViewsetAdmin, basename='amin-diffusion')
router.register('admin/avisouvrages', AvisSurOuvragesAdminViewsetAdmin, basename='amin-avis-ouvrage')
router.register('admin/ouvrages', OuvagesAdminViewset, basename='amin-ouvrage')

#route pour avis sur ouvrages
router.register('admin/fichieratacher', FichierAdminViewsetAdmin, basename='amin-fichier')
router.register('admin/document', DocumentsAdminViewsetAdmin, basename='amin-document')
router.register('admin/avis/document', AvisAdminViewset, basename='amin-avis')
#vue pour document et Avis
router.register('admin/filtres', FilterQuerysetAdminView, basename='admin-filtre')
router.register('admin/plan/destination', DestinationBatimentAdminViewsetAdmin, basename='admin-destination')
router.register('admin/planaffairefilter', TableauDeBordQuerysetAdminView, basename='admin-filter')
router.register('admin/ouvrage/destinations', DestinationBatimentAdminViewsetAdmin, basename='admin-destinations')
router.register('admin/media', MediaSerializerAdmin, basename='admin-missions')

router.register('admin/plan/affaire', PlanAffairesAdminViewsetAdmin, basename='admin-plan-affaire')
router.register('admin/ficheaffaire', FicheAffairesAdminViewsetAdmin, basename='admin-fichea-ffaire')
router.register('admin/product', ProductAdminViewsetAdmin, basename='admin-product')
router.register('admin/collaborateurs', CollaborateursAdminViewsetAdmin, basename='admin-collab')
router.register('admin/services', CbAdminViewsetAdmin, basename='admin-cb')
router.register('admin/missions', MissionsAdminViewsetAdmin, basename='admin-mission')
router.register('admin/intervention/technique', InterventionTechniqueAdminViewsetAdmin, basename='admin-it')
router.register('admin/marque', MarqueAdminViewsetAdmin, basename='admin-marque')
router.register('admin/client', ClientViewsetAdmin, basename='admin-client')
router.register('admin/entreprise/registration', EntrepriseAdminViewsetAdmin, basename='admin-entreprise-registration')
router.register('admin/entreprise/media/registration', MediaEntrepriseAdminViewsetAdmin,
                basename='admin-entreprise-media-registration')

urlpatterns = [
    path('api/connecte/users/<int:pk>/', UtilisateursConnectes.as_view({'get': 'list'}), name='connected-users'),
    path('api/get-csrf-token/', get_csrf_token, name='get_csrf_token'),
    path('admin/', admin.site.urls),
    path('api/medias/<int:charg_affaire_id>/medias/', MediaSerializerAdmin.as_view({'get': 'list'}), name='media-list'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/users/dj-rest-auth/', include('dj_rest_auth.urls')),  # new
    path('api/users/dj-rest-auth/registration/',  # new
        include('dj_rest_auth.registration.urls')),
]
