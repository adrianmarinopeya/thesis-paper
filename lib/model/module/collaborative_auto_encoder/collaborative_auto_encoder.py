import torch
import logging

from torch.nn               import Module, Linear, ReLU
from pytorch_common.modules import CommonMixin, FitMixin, PersistentMixin

from .collaborative_encoder         import CollaborativeEncoder
from .collaborative_decoder         import CollaborativeDecoder
from .latent_space_encoder          import LatentSpaceEncoder


class CollaborativeAutoEncoder(Module, FitMixin, PersistentMixin):
    def __init__(
        self,
        n_users,
        n_item_ratings,
        encoder_activation         = ReLU(),
        decoder_activation         = ReLU(),
        latent_space_dim    : int  = 256
    ):
        super(CollaborativeAutoEncoder, self).__init__()
        self.type = 'CollaborativeAutoEncoder'

        self.encoder = CollaborativeEncoder(
            n_users,
            n_item_ratings,
            encoder_activation,
            latent_space_dim
        )
        self.decoder = CollaborativeDecoder(
            n_item_ratings,
            decoder_activation,
            latent_space_dim
        )


    def forward(self, input_data, verbose=False):
        """
        input_data = (
            [batch_size, user_ids],
            [batch_size, [n_item_ratings]]
        )
        return [batch_size, [n_item_ratings]]
        """
        latent_space = self.encoder(input_data, verbose)
        return self.decoder(latent_space, verbose)


    def as_encoder(self):
        return LatentSpaceEncoder(self)