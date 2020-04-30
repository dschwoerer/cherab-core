# Copyright 2016-2018 Euratom
# Copyright 2016-2018 United Kingdom Atomic Energy Authority
# Copyright 2016-2018 Centro de Investigaciones Energéticas, Medioambientales y Tecnológicas
#
# Licensed under the EUPL, Version 1.1 or – as soon they will be approved by the
# European Commission - subsequent versions of the EUPL (the "Licence");
# You may not use this work except in compliance with the Licence.
# You may obtain a copy of the Licence at:
#
# https://joinup.ec.europa.eu/software/page/eupl5
#
# Unless required by applicable law or agreed to in writing, software distributed
# under the Licence is distributed on an "AS IS" basis, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied.
#
# See the Licence for the specific language governing permissions and limitations
# under the Licence.

from raysect.core.math.function import Function1D
from raysect.core.math.function import Function2D
from raysect.core.math.function import Function3D
from raysect.core.math.function import Constant1D, Constant2D, Constant3D
from raysect.core.math.function.vector3dfunction2d import Vector3DFunction2D as VectorFunction2D
from raysect.core.math.function.vector3dfunction2d import ConstantVector2D
from raysect.core.math.function.vector3dfunction2d import FloatToVector3DFunction2D as ScalarToVectorFunction2D
from .vectorfunction3d import VectorFunction3D, ConstantVector3D, ScalarToVectorFunction3D
